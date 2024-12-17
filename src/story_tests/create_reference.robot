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

A Article Reference Can Be Added And Seen On Start Page
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  Artikkeli1
    Set Author  author-testi
    Set Journal  test-journal
    Set Year  2021
    Set Volume  22
    Set Pages  8-9
    Click Button  Lisää
    Page Should Contain  Artikkeli1, author-testi, test-journal, 2021

A Inproceedings Reference Can Be Added And Seen On Start Page
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  Inpro1
    Set Author  author-testi
    Set Year  2022
    Set Booktitle  Inproname
    Click Button  Lisää
    Page Should Contain  Inpro1, author-testi, Inproname, 2022

Display Reference In Desired Form
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  Inpro1
    Set Author  author-testi
    Set Year  2022
    Set Booktitle  Inproname
    Click Button  Lisää
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  Artikkeli1
    Set Author  author-testi
    Set Journal  test-journal
    Set Year  2021
    Set Volume  22
    Set Pages  8-9
    Click Button  Lisää
    Click Link  Lisää uusi viite
    Click Button  Kirja
    Set Title  test
    Set Author  test-author
    Set Year  2000
    Click Button  Lisää
    Click Link  Näytä BibTeX muodossa
    Page Should Contain  @book
    Page Should Contain  @article
    Page Should Contain  @inproceedings

A book reference cannot be added without its mandatory fields
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Kirja
    Set Title  test-title
    Set Author  test-author
    Click Button  Lisää
    Page Should Contain  "Painovuosi" tulee esittää numeroina
    Set Title  test-title
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  "Kirjoittanut" ei voi olla tyhjä
    Set Author  test-author
    Set year  2000
    Click Button  Lisää
    Page Should Contain  "Teos" ei voi olla tyhjä

An article reference cannot be added without its mandatory fields
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  test-title
    Set Author  test-author
    Click Button  Lisää
    Page Should Contain  "Painovuosi" tulee esittää numeroina
    Set Title  test-title
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  "Kirjoittanut" ei voi olla tyhjä
    Set Author  test-author
    Set year  2000
    Click Button  Lisää
    Page Should Contain  "Artikkeli" ei voi olla tyhjä

An inproceedings reference cannot be added without its mandatory fields
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  test-title
    Set Author  test-author
    Click Button  Lisää
    Page Should Contain  "Painovuosi" tulee esittää numeroina
    Set Title  test-title
    Set Year  2000
    Click Button  Lisää
    Page Should Contain  "Kirjoittanut" ei voi olla tyhjä
    Set Author  test-author
    Set year  2000
    Click Button  Lisää
    Page Should Contain  "Otsikko" ei voi olla tyhjä

All fields on a book reference can be utilised
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Kirja
    Set Title  test-title
    Set Author  test-author
    Set Publisher  test-publisher
    Set Year  2000
    Set Volume  25
    Set Number  20
    Set Series  12
    Set Address  123
    Set Edition  2
    Set Month  July
    Set Note  test-note
    Set Annote  test-annote
    Click Button  Lisää
    Page Should Contain  test-title, test-author, test-publisher, 2000, 25, 20, 12, 123, 2, July, test-note, test-annote

All fields on an article reference can be utilised
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Artikkeli
    Set Title  test-title
    Set Author  test-author
    Set Journal  test-journal
    Set Year  2000
    Set Volume  25
    Set Pages  120-150
    Set Number  20
    Set Month  July
    Set Note  test-note
    Set Annote  test-annote
    Click Button  Lisää
    Page Should Contain  test-title, test-author, test-journal, 2000, 25, 20, 120-150, July, test-note, test-annote

All fields on an inproceedings reference can be utilised
    Go To Starting Page
    Click Link  Lisää uusi viite
    Click Button  Inproceedings
    Set Title  test-title
    Set Author  test-author
    Set Year  2000
    Set Booktitle  test-booktitle
    Set Editor  test-editor
    Set Volume  25
    Set Number  20
    Set Series  10
    Set Pages  120-150
    Set Address  test-address
    Set Organization  test-organization
    Set Publisher  test-publisher
    Set Month  July
    Set Note  test-note
    Set Annote  test-annote
    Click Button  Lisää
    Page Should Contain  test-title, test-author, test-booktitle, 2000, test-editor, 25, 20, 10, 120-150, July, test-address, test-organization, test-publisher, test-note, test-annote


*** Keywords ***