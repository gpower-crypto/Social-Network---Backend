# The Social Network Application Backend

Welcome to the backend of the Social Network Application! In this README, we'll take you on a journey through the various components that power the social network's backend.

## Table of Contents
- [Django Models](#django-models)
- [API Endpoints](#api-endpoints)
- [User Profile Management](#user-profile-management)
- [Posts and Comments](#posts-and-comments)
- [Friend Requests](#friend-requests)
- [Real-Time Chat](#real-time-chat)
- [Unit Testing](#unit-testing)
- [Deployment and Scalability](#deployment-and-scalability)

## Django Models
At the heart of the social network's backend are Django models. These models help organize and store essential data. Here's an overview of the models:

- **User Profiles:** User profiles store additional information like profile pictures, names, bios, locations, and status.
- **Posts:** Posts are user-generated content with text and timestamps.
- **Friend Requests:** The FriendRequest model manages friend requests between users.
- **Comments:** Comments link users and posts, containing text and timestamps.
- **Chat Messages:** ChatMessage handles real-time communication between users.

## API Endpoints
The backend offers various API endpoints for interacting with the application. Here are some key ones:

- User registration, profile retrieval, and status updates.
- User profile management.
- Post creation and retrieval.
- Managing friend requests.
- Comment creation, editing, and deletion.
- Real-time chat message creation and retrieval.

## User Profile Management
User profiles are central to the application, allowing users to express themselves. Here's how it works:

- **UserProfile Model:** It extends the built-in User model, including fields for profile pictures, names, bios, locations, and status.
- **Profile Editing:** Users can customize their profile information, including profile pictures, names, bios, locations, and status messages.

## Posts and Comments
Posts and comments enable user interactions on the platform:

- **Creating Posts:** Users can create posts, including text content and timestamps.
- **Commenting on Posts:** Users can engage with posts by adding comments, including user, post, text, and timestamps.

## Friend Requests
Building a network of friends is a core feature of the application. Here's how friend requests work:

- **Sending Friend Requests:** Users can send friend requests to others.
- **FriendRequest Model:** It tracks requests, including sender, recipient, and status (pending, accepted, or rejected).

## Real-Time Chat
Real-time chat enables users to communicate instantly with their friends:

- **Chat Messages:** Users can send and receive chat messages.
- **WebSocket Integration:** This technology ensures that chat messages are delivered instantly, creating a responsive chat environment.

## Unit Testing
Reliability is key. Comprehensive unit tests are included to ensure the application functions as expected. Tests cover user-related actions, posts, friends, comments, and chat messages.

## Deployment and Scalability
The application is deployed on AWS, ensuring both reliability and scalability. The frontend is hosted on AWS S3, while the backend is powered by AWS ECS and ECR. Scalability strategies include auto-scaling and load balancing.

Thank you for exploring the Social Network Application Backend. Enjoy using the platform!
