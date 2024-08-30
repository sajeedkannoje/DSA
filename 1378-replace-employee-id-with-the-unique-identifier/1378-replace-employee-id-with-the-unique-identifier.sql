select  en.unique_id , e.name from Employees e
left join EmployeeUNI en on en.id  = e.id 