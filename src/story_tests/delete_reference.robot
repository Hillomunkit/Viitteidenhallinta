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