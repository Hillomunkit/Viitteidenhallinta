*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Books

*** Test Cases ***
After creating a reference with only the mandatory fields, more fields can be filled
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Kirja
    Set Title  test-title
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  test-title, test-author, 2000
    Click Button  Muokkaa
    Set Publisher  test-publisher
    Set Volume  8
    Set Number  25
    Click Button  Tallenna muutokset
    Page Should Contain  test-title, test-author, test-publisher, 2000, 8, 25

Existing fields on a reference can be edited
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  test-article
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  test-article, test-author, 2000
    Click Button  Muokkaa
    Set Title  test-article2
    Set Year  1980
    Click Button  Tallenna muutokset
    Page Should Contain  test-article2, test-author, 1980



*** Keywords ***
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Number
    [Arguments]  ${number}
    Input Text  number  ${number}

