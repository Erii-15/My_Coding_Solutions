# Write your MySQL query statement below
Select name as Customers from Customers left join Orders 
on Orders.customerId=Customers.id
where Orders.id is null

-- LEFT JOIN includes every customer, even if they have no orders.
-- When there is no matching order, the Orders row is NULL.
-- Orders.id is NULL only for customers who never placed an order.
-- So filtering with "WHERE Orders.id IS NULL" returns customers with zero orders.
