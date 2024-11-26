*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Books

*** Test Cases ***
A book Reference Can Be Deleted
    Go To New Reference Page
    Set Title  test
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  test, test-author, 2000
    Click Button  Poista
    Page Should not Contain  test, test-author, 2000

A Article Reference Can Be Deleted
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
    Click Button  Poista
    Page Should Not Contain  Artikkeli1, author-testi, 2021

A Inproceedings Reference Can Be Deleted
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  Inpro1
    Set Author  author-testi
    Set Year  2022
    Set Booktitle  Inproname
    Click Button  Lisää
    Page Should Contain  Inpro1, author-testi, 2022
    Click Button  Poista
    Page Should Not Contain  Inpro1, author-testi, 2022

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