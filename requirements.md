## Functional Requirements

1. Login = Henry
2. Logout sceen = Alexander
3. Create new account = Alexander
4. Delete Account = Marcus
5. User home page (user can see messages of users they follow) = Marcus
6. Send message to followers  = Alexander
7. Multiple Sign Up Options (Email, Social Media) (Connect with any external API) = Shubham
8. Post image with Message = Shubham
9. Delete Post = Shubham
10. Password Reset = Marcus
11. Search = Henry
12. Users should be able to follow each other = Henry

## Non-functional Requirements
1. Optimized for 16:9 aspect ratio on chromium browsers
2. Having an anti-bot checking system
3. Dark Mode and Light Mode
4. Multilingual accessibility

## Use Cases

1. Send Messages to Followers

- **Pre-condition:** The user needs to be logged in

- **Trigger:** User selects "send tweet/message"

- **Primary Sequence:**

  1. The user will add and edit text inside a text box prompt
  2. When the user is satisified with what they have written, the user presses a send/submit button to publish their message

- **Primary Postconditions:** The user's followers will be able to see the new message

- **Alternate Sequence:**

  1. The user will add and edit text inside a text box prompt
  2. The user doesn't want to end up publishing their message, so they click a discard button to cancel publishing their message.
  3. The user will verify that they want to cancel publishing their message after seeing that their message content won't be saved.

2. Enforce a Character Limit for messages

- **Pre-condition:** The user has their message written.

- **Trigger:** The user has entered more than 140 characters for a message or the user clicks post message

- **Primary Sequence:**

  1. The user enters more than 140 charaters in their message.
  2. Red text will appear on the screen letting the user know that the have gone over the character limit.
  3. A number showing the amount of extra characters will show up.
  4. The user deletes enough characters to be within 140 characters or less
  5. The user clicks on the "post message" button


- **Primary Postconditions:** The message is posted to their profile.

- **Alternate Sequence:**
  1. The user enters more than 140 charaters in their message.
  2. Red text will appear on the screen letting the user know that the have gone over the character limit.
  3. A number showing the amount of extra characters will show up.
  4. The user tries to post their message.
  5. Another popup will show to grab the user's attention stating that the message
  failed to publish
  6. The user deletes enough characters to be within 140 characters or less
  7. The user clicks on the "post message" button

- **Alternate Sequence:**

3. Post image with message

- **Pre-condition:** The user is logged in

- **Trigger:** User selects "send tweet/message"

- **Primary Sequence:**

  1. System has a upload image prompt and text box
  2. Users can upload multiple image files into the image prompt
  3. User can add and edit text inside a text box
  4. System checks that the message is within the word limit
  5. User can press a send button
  6. System communicates with servers to upload the images and message
  7. System ensures the image and message can appear on user profile
  8. Followers will be able to see the images and message

- **Primary Postconditions:** A message appears that followers can read

- **Alternate Sequence:**

  1. The user is unable to send the image
  2. The message will no send to servers and followers cannot see the image

- **Alternate Sequence:**

  1. The servers fail to update
  2. Followers cannot see the image

4. Delete Post
- **Pre-condition:** The user adds a post

- **Trigger:** User selects "delete post"

- **Primary Sequence:**

  1. When the user selects the menu next to the post, an option menu is printed 
  2. User selects "delete post"
  3. System checks for where the post is stored in the database and removes it from the store

- **Primary Postconditions:** A message appears reading "Successful Deletion"

- **Alternate Sequence:**

  1. The user is unable to delete their post
  2. The message will not delete from the database and followers still see the post

5. Password Reset
- **Pre-condition:** The user is logged in

- **Trigger:** User selects "change my password"

- **Primary Sequence:**

  1. User clicks on their profile and a menu drop down appears
  2. User selects "change my password"
  3. User is prompted to enter their old password followed by their new password
  4. System assigns a new hash for the new password and pairs it with the user's login information

- **Primary Postconditions:** A message appears reading "Successful Password Reset"

- **Alternate Sequence:**

  1. The user enters the same password as their old one
  2. The System will prompt to enter a new password

6. Users should be able to follow each other

- **Pre-condition:** The user is logged in

- **Trigger:** User clicks on "add friend" button

- **Primary Sequence:**

  1. Drop down box to search for users appears
  2. User types in name of friend he wants to add and hits search
  3. A list of matches for users appears on the screen
  4. User then finds the profile, and clicks the "send friend request" button to the right of the name
  5. System sends a friend request notification to the user that was chosen
  6. The user who recieved the friend request will get a notification on their home page
  7. They can click the notification and get the choice to accept or decline it

- **Primary Postconditions:** If the user accepted, they are now added as a friend and their posts will appear on the users home page

- **Alternate Sequence:**

  1. User enters and searches for a person they are already friends with
  2. When the user is found, the option to "send friend request" will be greyed out

- **Alternate Sequence:**

  1. User searches for someone to add that does not exist
  2. A notice saying "No user found" will appear to notify that name does not exist