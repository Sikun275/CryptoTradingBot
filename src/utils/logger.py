import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
if not os.path.exists('data/logs'):
    os.makedirs('data/logs')

# Set up logging
log_file = f"data/logs/bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)