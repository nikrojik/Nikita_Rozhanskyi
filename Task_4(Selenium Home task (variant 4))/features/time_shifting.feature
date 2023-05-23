Feature: Time shifting test om OrangeHRM

  Scenario: Time shifting normal-flow
    Given we have driver initialized
    When we login successfully
     And we go to time shift panel
     And we add new time shift
    Then we have new time shift appeared
     And we remove row