package main

import "fmt"

func main() {
   THREADCOUNT := 20
   primeList:=make([]int,0,4000)
   sentCount:=0
   recvCount:=0
   chani := make(chan int)
   var tempi int

   for i:=2; i<50000000; i++ {
      if sentCount - recvCount < THREADCOUNT {
         sentCount+=1
         go checkPrime(i, chani)
      } else {
         emptyChannel := false
         for emptyChannel!= true {
            select {
               case tempi = <-chani:
                  recvCount+=1
                  if tempi!=0 {
                     primeList=append(primeList, tempi)
                     if len(primeList) % 10000 ==0 {
                        fmt.Println(i)
                     }
                  }
               default:
                  emptyChannel = true
            }
         }
         i-= 1
      }
   }
   fmt.Println(primeList)
}


func checkPrime(i int, chani chan int) bool {
   checkCount := 0

   for c:=2; c<i/2; c++ {
      if i%c == 0 {
         checkCount+=1
         break
      }
   }
   if checkCount==0 {
      chani <- i
      return true
   } else {
      chani <- 0
      return false
   }
}
