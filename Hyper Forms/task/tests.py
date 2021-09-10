import os

import requests
from hstest import *


class HyperFormsSavingFormDataTest(DjangoTest):
    use_database = True

    def get_index_with_no_participants(self) -> CheckResult:
        index = self.read_page(self.get_url())
        if all(x in index.lower() for x in ["no participants","be the first"]):
            return CheckResult.correct()
        else:
            return CheckResult.wrong("Seems like there is no line telling the first visitor to become the first participant...")

    def fill_in_the_form(self) -> CheckResult:
        register_page = requests.get(self.get_url('register'))
        filled_form = requests.post(self.get_url('register/'), cookies={"csrftoken": register_page.cookies.get("csrftoken")},
                                    data={"csrfmiddlewaretoken": register_page.cookies.get("csrftoken"),
                                          "name": "Boba", "age": "22", "favorite_book": "Kuka"})
        index = self.read_page(self.get_url())
        if all(x in index.lower() for x in ["name", "age", "favorite book", "boba", "22","kuka"]):
            if all(x not in index.lower() for x in ["no participants", "be the first"]):
                return CheckResult.correct()
            else:
                return CheckResult.wrong("If there are participants in the club, the page should not tell people there are no participants!")
        else:
            return CheckResult.wrong("Cannot see the inserted form data on the main page!")

    @dynamic_test(order=1)
    def test_get_index_no_participants(self):
        return self.get_index_with_no_participants()

    @dynamic_test(order=2)
    def test_post_form(self):
        return self.fill_in_the_form()


if __name__ == '__main__':
    HyperFormsSavingFormDataTest().run_tests()
