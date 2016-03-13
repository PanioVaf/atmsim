Feature: Testing ATM Withdraw
    In this test we are testing
    

    Scenario: Withdraw bigger amount than total
        Given ATM has 3 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw amount of 180 dollars
        Given ATM has 6 notes of twenty dollars
        Given ATM has 6 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then ATM gives me 4 twenty notes and 2 fifty notes

