*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Books

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Title Should Be  Viitteidenhallinta
    Page Should Contain Link  Lisää uusi viite

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Set Title  test
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  test, test-author, 2000

After adding two references, there are two
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Set Title  test1
    Set Author  test-author
    Set Year  2001
    Click Button  Lisää
    Click Link  Lisää uusi viite
    Set Title  test2
    Set Author  author-test
    Set Year  2002
    Click Button  Lisää
    Page Should Contain  test1, test-author, 2001
    Page Should Contain  test2, author-test, 2002

A article reference can be added and seen on start page
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  Artikkeli1
    Set Author  author-testi
    Set Journal  test-journal
    Set Year  2021
    Set Volume  22
    Set Pages  8--9
    Click Button  Lisää
    Page Should Contain  Artikkeli1, author-testi, 2021

A Inproceedings reference can be added and seen on start page
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  Inpro1
    Set Author  author-testi
    Set Year  2022
    Set Booktitle  Inproname
    Click Button  Lisää
    Page Should Contain  Inpro1, author-testi, 2022

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