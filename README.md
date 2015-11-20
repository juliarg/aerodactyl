# aerodactyl

A website helping Columbia University students find and share temporary housing and storage space!!

Three classes of objects stored in relational database: 

1) User
  - name, email, contact info 
  - Listings 
  - Requests 
  - Gender 
  Functions: 
    - Make listing active/inactive 
    - Make user account inactive 
    - Change info 
  
2) Listing
  Attributes: 
    - address
    - duration of stay
    - start & end dates
    - user posted 
    - boolean active 
    - payment*
    - contract*
    - photos*
  Functions: 
    On construction: 
      - add to listings
      - make active
      - add to activity class 
    - make active/inactive
    - add to requests 

3) Request (join table) 
  Attributes: 
    - Listing 
    - fromUser
    - toUser
    - resolved (i.e. request was accepted) 
