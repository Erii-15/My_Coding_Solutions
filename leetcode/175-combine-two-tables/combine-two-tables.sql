# Write your MySQL query statement below
Select firstName,lastName,city,state
from Person left join Address 
#Left join because you want things that exist in left hand side regardless of it exists on right hand side
on Person.personId=Address.personId