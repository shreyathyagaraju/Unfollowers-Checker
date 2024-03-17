from bs4 import BeautifulSoup
import zipfile
import os

def extract_usernames(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        usernames = [a.text for a in soup.find_all('a', href=True)]
    return usernames

def find_unfollowers(followers, following):
    unfollowers = [user for user in following if user not in followers]
    return unfollowers

def main():
    # Path to the zip file
    zip_file_path = "ayeitsshreya data.zip"
    # Extracting the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall("temp_folder")

    followers_file = "temp_folder/connections/followers_and_following/followers_1.html"
    following_file = "temp_folder/connections/followers_and_following/following.html"

    followers = extract_usernames(followers_file)
    following = extract_usernames(following_file)

    unfollowers = find_unfollowers(followers, following)

    print("Users who are not following you back:")
    for user in unfollowers:
        print(user)

    # Clean up temporary files
    os.remove(followers_file)
    os.remove(following_file)
    os.rmdir("temp_folder/connections/followers_and_following")
    os.rmdir("temp_folder/connections")
    os.rmdir("temp_folder")

if __name__ == "__main__":
    main()



