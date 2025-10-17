package main

import (
  "fmt"
  "sort"
)

func main() {
  var budgets []int
  var totalBudget = 0

  var nbParticipants int
  fmt.Scan(&nbParticipants)
  
  var giftPrice int
  fmt.Scan(&giftPrice)
  
  for i := 0; i < nbParticipants; i++ {
    var budget int
    fmt.Scan(&budget)
    budgets = append(budgets, budget)
    totalBudget += budget
  }

  if totalBudget < giftPrice {
    fmt.Println("IMPOSSIBLE")
  } else {
    sort.Ints(budgets)
    for i := 0; i < nbParticipants; i++ {
      var contribution = budgets[i]
      var maxContribution = giftPrice / (nbParticipants - i)
      if contribution >= maxContribution {
        contribution = maxContribution
      }
      fmt.Println(contribution)
      giftPrice -= contribution
    }
  }
}