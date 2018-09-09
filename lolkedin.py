from selenium import webdriver as wd;
import sys, os;
import time;
import sys;
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        ElementNotSelectableException,
                                        ElementNotVisibleException,
                                        ErrorInResponseException,
                                        InsecureCertificateException,
                                        InvalidCoordinatesException,
                                        InvalidElementStateException,
                                        InvalidSessionIdException,
                                        InvalidSelectorException,
                                        ImeNotAvailableException,
                                        ImeActivationFailedException,
                                        InvalidArgumentException,
                                        InvalidCookieDomainException,
                                        JavascriptException,
                                        MoveTargetOutOfBoundsException,
                                        NoSuchCookieException,
                                        NoSuchElementException,
                                        NoSuchFrameException,
                                        NoSuchWindowException,
                                        NoAlertPresentException,
                                        ScreenshotException,
                                        SessionNotCreatedException,
                                        StaleElementReferenceException,
                                        TimeoutException,
                                        UnableToSetCookieException,
                                        UnexpectedAlertPresentException,
                                        UnknownMethodException,
                                        WebDriverException)



pagenumber = sys.argv[1] # arguments to pass - page number
extractor = 1; # extractor
#
# Press CTRL+C to stop the script
#

print ("Example of usage: \n")
print ("python lolkedin.py 22 pentest example@example.com B00bsterpassw0rd \n")
print ("First argument stands for page number you want to start, second one is keyword and login/password \n")


searchstring = sys.argv[2]	# keyword
username = sys.argv[3]		# 
password = sys.argv[4]		# 	

firefox = wd.Firefox ();
firefox.get ('https://linkedin.com/');


firefox.find_element_by_id ('login-email').send_keys (username);
firefox.find_element_by_id ('login-password').send_keys (password);
firefox.find_element_by_id ('login-submit').click ();



pagenumberint = int(pagenumber);
extractorint = int(extractor);


def findconnect (pagenumberint,extractorint):
	firefox.get ('https://www.linkedin.com/search/results/index/?keywords='+str(searchstring)+'&origin=GLOBAL_SEARCH_HEADER&page='+str(pagenumberint)+'');
	time.sleep(5)
	firefox.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')["+str(extractorint)+"].click();")
	time.sleep(5)
	sendnow = firefox.find_element_by_css_selector(".button-primary-large.ml1")
	firefox.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", sendnow)
	time.sleep(4)
	return

def fireball(pagenumberint,extractorint):
	try:
		while extractorint < 6:
			findconnect(pagenumberint,extractorint);

			if extractorint == 5:
				extractorint = 0;
				print ("we are here");
			extractorint+=1

	except (NoSuchElementException,JavascriptException):
		print ("Navigating to another page #: "+str(pagenumberint)+"");
		pagenumberint+=1
		fireball(pagenumberint,1);
		pass
	return

fireball(pagenumberint,extractorint);

firefox.close();



