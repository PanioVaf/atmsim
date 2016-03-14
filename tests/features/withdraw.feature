Feature: Testing ATM Withdraw
    In this test we are testing
    

    Scenario: Withdraw invalid and bigger amount than total
        Given ATM has 3 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw invalid and smaller amount than total
        Given ATM has 6 notes of twenty dollars
        Given ATM has 6 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 145 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw valid amount 
        Given ATM has 6 notes of twenty dollars
        Given ATM has 6 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then ATM gives me 4 twenty notes and 2 fifty notes
 
    Scenario: Withdraw invalid amount with zero total
        Given ATM has 0 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 145 dollars
        Then I see the message I cannot withdraw this amount

   Scenario: Withdraw valid amount with zero balance
        Given ATM has 0 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 100 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw invalid amount lower than notes
        Given ATM has 2 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 10 dollars
        Then I see the message I cannot withdraw this amount


    Scenario: Double Withdraw invalid and bigger amount than total
        Given ATM has 3 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 1800 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Double Withdraw invalid and smaller amount than total
        Given ATM has 20 notes of twenty dollars
        Given ATM has 10 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 145 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 15 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Double Withdraw valid amount 
        Given ATM has 10 notes of twenty dollars
        Given ATM has 20 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then ATM gives me 4 twenty notes and 2 fifty notes
        When I try to withdraw 200 dollars
        Then ATM gives me 5 twenty notes and 2 fifty notes
 
    Scenario: Double Withdraw invalid amount with zero total
        Given ATM has 0 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 145 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 225 dollars
        Then I see the message I cannot withdraw this amount

   Scenario: Double Withdraw valid amount with zero balance
        Given ATM has 0 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 100 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 20 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Double Withdraw invalid amount lower than notes
        Given ATM has 2 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 10 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 30 dollars
        Then I see the message I cannot withdraw this amount


    Scenario: Withdraw valid amount, Withdraw invalid and bigger amount than total
        Given ATM has 5 notes of twenty dollars
        Given ATM has 3 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 180 dollars
        Then ATM gives me 4 twenty notes and 2 fifty notes
        When I try to withdraw 100 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw valid amount, Withdraw invalid and smaller amount than total
        Given ATM has 20 notes of twenty dollars
        Given ATM has 10 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 100 dollars
        Then ATM gives me 0 twenty notes and 2 fifty notes
        When I try to withdraw 15 dollars
        Then I see the message I cannot withdraw this amount
 
    Scenario: Withdraw valid amount, Withdraw invalid amount with zero total
        Given ATM has 0 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 120 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 225 dollars
        Then I see the message I cannot withdraw this amount

    Scenario: Withdraw valid amount with zero 20 notes
        Given ATM has 0 notes of twenty dollars
        Given ATM has 2 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 50 dollars
        Then ATM gives me 0 twenty notes and 1 fifty notes

    Scenario: Withdraw valid amount with zero 50 notes
        Given ATM has 2 notes of twenty dollars
        Given ATM has 0 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 20 dollars
        Then ATM gives me 1 twenty notes and 0 fifty notes

    Scenario: Triple Withdraw valid -invalid -valid
        Given ATM has 2 notes of twenty dollars
        Given ATM has 3 notes of fifty dollars
        Given ATM has been initialised with a deposit
        When I try to withdraw 20 dollars
        Then ATM gives me 1 twenty notes and 0 fifty notes        
        When I try to withdraw 30 dollars
        Then I see the message I cannot withdraw this amount
        When I try to withdraw 50 dollars
        Then ATM gives me 0 twenty notes and 1 fifty notes



