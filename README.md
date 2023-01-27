# Customer_app	
**http://localhost:8000/customer/api/customer/**
**http://localhost:8000/customer/api/ticket_booking/**
* booking_history -> Modify upcoming bookings as long as start time is 30mins more than current date time
* movie_choice -> Choose from available movies (as per movie time slot and audi location)	Choose from available movies
* customer_details -> CRUD customer credentials	
* book_tickets -> seats_booked * ticket_price (updated as per audi and movie title) 
 
# Admin_app	
**http://localhost:8000/administrator/api/audi_dist/**
**http://localhost:8000/administrator/api/movie_dist/**
* movies_list -> [(movie_title_name, movie_duration)] -> Movie titles and duration list
* movie_dist -> Define movie listings and distribution in audis (CRUD)
* customer_list	-> Customer Contact info list
* total_income	-> booking_history for all customers