from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_setup_some_simulations(self):
        # Tom wants to view and manage his currently running optical/electrical
        # simulations. He opens the 'OCTODEPS' simulation dashboard
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention OCTODEPS
        self.assertIn('OCTODEPS', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('OCTODEPS', header_text)

        # The page is divided into 3 sections: Optical simulations,
        # electrical simulations and results.
        opt = self.browser.find_element_by_id('id_opt_sims_div')
        elc = self.browser.find_element_by_id('id_elc_sims_div')
        res = self.browser.find_element_by_id('id_results_div')

        self.assertIn('Optical simulations',opt.find_element_by_tag_name('h2').text)
        self.assertIn('Electrical simulations',elc.find_element_by_tag_name('h2').text)
        self.assertIn('Results',res.find_element_by_tag_name('h2').text)

        # In first div, 3 empty lists of optical simulations are displayed:
        # to setup, to run and to analyse.
        opt_to_setup   = opt.find_element_by_id('id_opt_to_setup')
        opt_to_run     = opt.find_element_by_id('id_opt_to_run')
        opt_to_analyse = opt.find_element_by_id('id_opt_to_analyse')

        self.assertIn('To setup',opt_to_setup.find_element_by_tag_name('h3').text)
        self.assertIn('To run',opt_to_run.find_element_by_tag_name('h3').text)
        self.assertIn('To analyse',opt_to_analyse.find_element_by_tag_name('h3').text)

        # In second div, 3 empty lists of electrical simulations are displayed:
        # to setup, to run and to analyse.
        elc_to_setup   = elc.find_element_by_id('id_elc_to_setup')
        elc_to_run     = elc.find_element_by_id('id_elc_to_run')
        elc_to_analyse = elc.find_element_by_id('id_elc_to_analyse')

        self.assertIn('To setup',elc_to_setup.find_element_by_tag_name('h3').text)
        self.assertIn('To run',elc_to_run.find_element_by_tag_name('h3').text)
        self.assertIn('To analyse',elc_to_analyse.find_element_by_tag_name('h3').text)

        # There are 4 buttons. Go, Stop, Clear and Plot.
        self.browser.find_element_by_id('id_go_button')
        self.browser.find_element_by_id('id_stop_button')
        self.browser.find_element_by_id('id_clear_button')
        self.browser.find_element_by_id('id_plot_button')

        # Tom wants to initialise some simulations (jobs) without setting them up.
        # He sets the following parameters:
        # isolated coated nanowires
        # TiO2 (n=3 dielectric) core, CdSe coating
        # a = [160,170,180,190,200]
        # th = [30]
        # l = [1000]
        self.fail('Finish the test!')

        # He initially sets opt_create_flag = True.

        # Tom clicks on the Go button. The page refreshes and shows that some
        # simulations have appeared in the list "To setup" under "Optical
        # simulations", with a single dot next to each to show that its primed.

        # Tom wants to now setup the simulations. He sets
        # opt_create_flag = False and then sets opt_setup_flag = True.

        # Tom clicks on Go. The simulations start setting up. The single dot
        # next to each simulation in the "To Setup" list turns into double
        # dots, indicating that they're being setup.

        # 5 new simulations appear in "To Run" list, with single dots.

        # The results section shows a plot of the refractive index of each
        # material used in the simulations.

        # Tom wants to run the simulations. He sets opt_run_flag = True and the
        # other flags to false.

        # Tom clicks on Go. The 5 simulations start running. One has double
        # dots next to it, the other 4 have single dots.

        # After a while, the first simulation appears in the "To Analyse" list
        # and disappears from the "To Run" list. 4 simulations are left,
        # 1 with double dots.

        # After a while, the 2nd simulation appears in the "To Analyse" list
        # which now has 2 simulations in it. 3 simulations are left in "To Run"
        # 1 with double dots.

        # After a while, the 3rd simulation appears in the "To Analyse" list
        # which now has 3 simulations in it. 2 simulations are left in "To Run"
        # 1 with double dots.

        # After a while, the 4th simulation appears in the "To Analyse" list
        # which now has 4 simulations in it. 1 simulations is left in "To Run"
        # with double dots.

        # After a while, there are no simulations left in "To Run" and 5
        # simulations in "To Analyse", all with single dots.

        # Tom wants to analyse the simulations. He sets opt_analyse_flag = True
        # and the other flags to False.

        # Tom clicks on Go. Next to each simulation the double dots appear one
        # by one. Then the simulations disappear from the list and appear in
        # the "To Setup" list under "Electrical Simulations".

        # The results section shows a plot of Mie Absorption efficiency, Qabs,
        # against wavelength for each of the simulations (different colours
        # for each).

        # Tom clicks on the Plot button. The Qabs plot in the results section
        # is saved as results.png.

        # Satisfied, he goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')