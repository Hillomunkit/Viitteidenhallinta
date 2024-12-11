*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database and Add Test References

*** Test Cases ***
Filtering by reference type works
    Test Book Is Visible
    Test Article Is Visible
    Test Inproceedings Is Visible
    Unselect Checkbox  book
    Test Book Is Not Visible
    Unselect Checkbox  article
    Test Article Is Not Visible
    Unselect Checkbox  inproceedings
    Test Inproceedings Is Not Visible

Filtering By Keyword works
    Test Book Is Visible
    Test Article Is Visible
    Test Inproceedings Is Visible
    Set Search Keyword  book
    Test Book Is Visible
    Test Article Is Not Visible
    Test Inproceedings Is Not Visible
    Set Search Keyword  inproceedings
    Test Book Is Not Visible
    Test Article Is Not Visible
    Test Inproceedings Is Visible
    Set Search Keyword  orava
    Test Book Is Not Visible
    Test Article Is Not Visible
    Test Inproceedings Is Not Visible

*** Keywords ***

Reset Database and Add Test references
    Reset Books
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Kirja
    Set Title  test-book
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  test-article
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  test-inproceedings
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää

Test Book Is Visible
    Element Should Be Visible  xpath://*[contains(text(), "test-book, test-author, 2000")]

Test Article Is Visible
    Element Should Be Visible  xpath://*[contains(text(), "test-article, test-author, 2000")]

Test Inproceedings Is Visible
    Element Should Be Visible  xpath://*[contains(text(), "test-inproceedings, test-author, 2000")]

Test Book Is Not Visible
    Element Should Not Be Visible  xpath://*[contains(text(), "test-book, test-author, 2000")]

Test Article Is Not Visible
    Element Should Not Be Visible  xpath://*[contains(text(), "test-article, test-author, 2000")]

Test Inproceedings Is Not Visible
    Element Should Not Be Visible  xpath://*[contains(text(), "test-inproceedings, test-author, 2000")]

Set Search Keyword
    [Arguments]  ${word}
    Input Text  search  ${word}