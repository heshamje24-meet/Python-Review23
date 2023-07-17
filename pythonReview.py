def create_youtube_video(title, description, hashtags):
    video = { "title": title,"description": description,"likes": 0,"dislikes": 0,"comments": {},"hashtags": hashtags[:5]
    }
    return video

def like(video):
    if "likes" in video:
        video["likes"] += 1
    return video

def dislike(video):
    if "dislikes" in video:
        video["dislikes"] += 1
    return video

def add_comment(video, username, comment_text):
    if "comments" in video:
        video["comments"][username] = comment_text
    return video

def similarity_to_video(video1, video2):
    common_hashtags = set(video1["hashtags"]) & set(video2["hashtags"])
    similarity_percentage = (len(common_hashtags) / len(video1["hashtags"])) * 100
    return similarity_percentage



video1 = create_youtube_video("Video 1", "Description 1", ["funny", "comedy", "cats"])
video2 = create_youtube_video("Video 2", "Description 2", ["comedy", "dogs"])

print("Video 1:", video1)
print("Video 2:", video2)

video1 = like(video1)
video1 = like(video1)
video2 = dislike(video2)

print("Video 1 after likes:", video1)
print("Video 2 after dislikes:", video2)

video1 = add_comment(video1, "User1", "Great video!")
video2 = add_comment(video2, "User2", "I didn't like it.")

print("Video 1 after comment:", video1)
print("Video 2 after comment:", video2)

similarity = similarity_to_video(video1, video2)
print("Similarity between Video 1 and Video 2:", similarity)

