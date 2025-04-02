import threading
import os
import time
import requests


def download_image(url, index, folder):
    """Download an image and save it to the specified folder."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code != 200:
        print(f"Failed to download {url} - HTTP {response.status_code}")
        return

    file_path = os.path.join(folder, f"image_{index}.jpg")

    # Write image to file in chunks
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print(f"Downloaded: {file_path} ({file_size} bytes)")


def download_without_threading(urls, folder):
    """Sequential download without threading."""
    start_time = time.time()
    for i, url in enumerate(urls):
        download_image(url, i, folder)
    return time.time() - start_time


def download_with_threading(urls, folder):
    """Download using threading."""
    start_time = time.time()
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_image, args=(url, i, folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return time.time() - start_time


if __name__ == "__main__":
    # List of image URLs to download
    urls = [
        "https://unsplash.com/photos/CTflmHHVrBM/download?force=true",
        "https://unsplash.com/photos/pWV8HjvHzk8/download?force=true",
        "https://unsplash.com/photos/1jn_3WBp60I/download?force=true",
        "https://unsplash.com/photos/8E5HawfqCMM/download?force=true",
        "https://unsplash.com/photos/yTOkMc2q01o/download?force=true",
    ]

    # Directories to save images
    sequential_path = os.path.join(os.getcwd(), "downloaded_images_sequential")
    threading_path = os.path.join(os.getcwd(), "downloaded_images_threading")
    os.makedirs(sequential_path, exist_ok=True)
    os.makedirs(threading_path, exist_ok=True)

    print(f"Running tests on {len(urls)} images...")

    print("\nRunning without threading...")
    single_time = download_without_threading(urls, sequential_path)

    print("\nRunning with threading...")
    multi_time = download_with_threading(urls, threading_path)

    # Compare the results
    print("\nResults:")
    print(f"Without threading: {single_time:.2f} seconds")
    print(f"With threading: {multi_time:.2f} seconds")
    print(f"Speedup: {single_time / multi_time:.2f}x")
