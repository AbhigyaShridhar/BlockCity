All of the back-end has been implemented in the [BlockCity/slam_dunks](https://github.com/AbhigyaShridhar/BlockCity/tree/main/slam_dunks) directory




# BlockCity API:

## _This is the documentation for Api routes this application is going to use:

- A list of all the registered users and data regarding them:
```shell
    users/
  ```

- Detailed information about a single user:
```shell
    users/<Integer:User_Id>
  ```
  
- Finish a game and enter who won so that XPs can be updated
```shell
    gameover/<int:id_of_the_winning_team>/<int:id_of_the_match>
  ```
  This will award XPs to the winning team and check if they are eligible for a level up
  and Update the instances of the Venue and Match models (Winner, Number of games played and won)
  
- Schedule a New Match:
 ```shell
    matches/new/schedule
  ```
  This will allow a user to schedule a new match with another team's captain after deciding on the date and city
  
- Browse through cities or register your city if signed in:
  ```shell
    browse/city
  ```
  
- Browse through venues around a particular city or nominate one if logged in:
   ```shell
    browse/venue
  ```
  
- Register an account as a team captain:
    ```shell
    users/auth/register
  ```
  
- Login to an existing accout:
    ```shell
    users/auth/login/
  ```
  
- Logout from an account:
    ```shell
    users/auth/logout/
  ```
  
  The last two URL routes only work with POST method, to log in or log out a user
