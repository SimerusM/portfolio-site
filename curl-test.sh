#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:5000/api/timeline_post"

# Create a new post
create_response=$(curl -s -X POST -d "name=random&email=random@gmail.com&content=randomcontext" $BASE_URL)
echo "Create response: $create_response"

# Extract the new post ID of the create response using jq (json parser)
new_post_id=$(echo $create_response | jq -r '.id')

# Get all posts
get_response=$(curl -s -X GET $BASE_URL)
echo "All posts: $get_response"

# Delete the newly created post
delete_response=$(curl -s -X DELETE -d "id=$new_post_id" "$BASE_URL")
echo "Delete response: $delete_response"
