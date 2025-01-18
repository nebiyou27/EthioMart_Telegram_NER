import csv
import os
from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables
load_dotenv()

# Get API credentials from the .env file
api_id = int(os.getenv('API_ID'))  
api_hash = os.getenv('API_HASH')

# Output directory
output_dir = "data/scraped_channels/"
os.makedirs(output_dir, exist_ok=True)

# Function to scrape a channel (including messages with media)
async def scrape_channel_text_only(client, channel_name, writer):
    print(f"Scraping messages from {channel_name}...")
    entity = await client.get_entity(channel_name)
    channel_title = entity.title  # Extract the channel's title
    async for message in client.iter_messages(channel_name):  
        if message.text:  # Only check for text content, no media filter
            writer.writerow([channel_title, channel_name, message.id, message.text, message.date])

# Initialize the client
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()
    
    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date'])  # Include channel title in the header
        
        # List of channels to scrape
        channels = [
            "@ZemenExpress",
            "@nevacomputer",
            "@Leyueqa",
            "@forfreemarket",
            "@AwasMart"
        ]
        
        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            await scrape_channel_text_only(client, channel, writer)
            print(f"Scraped data from {channel}")

with client:
    client.loop.run_until_complete(main())
