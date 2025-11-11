"""
Configuration file for ProBot Telegram Bot
Easy customization and settings management
"""

import os
from typing import Dict, List

class BotConfig:
    """Bot configuration class with all settings"""
    
    # Bot Information
    BOT_NAME = "ProBot"
    BOT_VERSION = "1.0.0"
    BOT_DESCRIPTION = "Professional Telegram Bot with AI features"
    
    # Admin Settings
    ADMIN_IDS = [
        123456789,  # Replace with your Telegram user ID
        # Add more admin IDs as needed
    ]
    
    # Bot Features - Enable/Disable features
    FEATURES = {
        'ai_chat': True,
        'file_processing': True,
        'user_management': True,
        'analytics': True,
        'admin_panel': True,
        'welcome_message': True,
        'smart_responses': True,
        'photo_handling': True,
        'document_handling': True,
    }
    
    # Response Settings
    RESPONSES = {
        'ai_enabled': True,
        'default_language': 'en',
        'response_delay': 0.5,  # seconds
        'typing_indicator': True,
    }
    
    # File Processing Settings
    FILE_SETTINGS = {
        'max_file_size': 10 * 1024 * 1024,  # 10MB
        'allowed_file_types': ['.pdf', '.txt', '.doc', '.docx', '.jpg', '.png'],
        'save_uploads': True,
        'upload_path': 'uploads/',
    }
    
    # Analytics Settings
    ANALYTICS = {
        'track_user_activity': True,
        'track_commands': True,
        'track_file_uploads': True,
        'daily_stats': True,
    }
    
    # Security Settings
    SECURITY = {
        'rate_limit_enabled': True,
        'max_requests_per_minute': 30,
        'ban_spam_users': True,
        'log_all_activity': True,
    }
    
    # Custom Messages
    MESSAGES = {
        'welcome': "🤖 Welcome to ProBot! Your professional assistant is ready to help.",
        'help': "📚 Use /help to see available commands and features.",
        'unknown_command': "❓ Unknown command. Type /help to see available commands.",
        'file_received': "📁 File received and processed successfully!",
        'photo_received': "📸 Photo received and analyzed!",
        'admin_only': "🔒 This command is available to administrators only.",
    }
    
    # External API Settings (for future enhancements)
    APIS = {
        'openai_api_key': os.environ.get('OPENAI_API_KEY', ''),
        'weather_api_key': os.environ.get('WEATHER_API_KEY', ''),
        'news_api_key': os.environ.get('NEWS_API_KEY', ''),
    }
    
    @classmethod
    def get_admin_ids(cls) -> List[int]:
        """Get list of admin user IDs"""
        return cls.ADMIN_IDS
    
    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        """Check if user is admin"""
        return user_id in cls.ADMIN_IDS
    
    @classmethod
    def is_feature_enabled(cls, feature: str) -> bool:
        """Check if a feature is enabled"""
        return cls.FEATURES.get(feature, False)
    
    @classmethod
    def get_message(cls, message_key: str) -> str:
        """Get custom message by key"""
        return cls.MESSAGES.get(message_key, "Message not found")
    
    @classmethod
    def validate_config(cls) -> Dict[str, bool]:
        """Validate configuration settings"""
        validation_results = {
            'admin_ids_set': len(cls.ADMIN_IDS) > 0 and cls.ADMIN_IDS[0] != 123456789,
            'bot_token_set': 'TELEGRAM_BOT_TOKEN' in os.environ,
            'features_configured': len(cls.FEATURES) > 0,
            'file_settings_valid': cls.FILE_SETTINGS['max_file_size'] > 0,
            'security_enabled': cls.SECURITY['rate_limit_enabled'],
        }
        return validation_results

# Quick setup configurations for different use cases
class QuickSetup:
    """Quick setup configurations for different bot types"""
    
    @staticmethod
    def business_bot():
        """Configuration for business/customer support bot"""
        return {
            'features': {
                'ai_chat': True,
                'file_processing': True,
                'user_management': True,
                'analytics': True,
                'admin_panel': True,
                'welcome_message': True,
                'smart_responses': True,
                'photo_handling': True,
                'document_handling': True,
            },
            'messages': {
                'welcome': "🤖 Welcome to our business bot! How can we help you today?",
                'help': "📚 Our support team is here to help. Use /help to see available commands.",
            }
        }
    
    @staticmethod
    def community_bot():
        """Configuration for community/group management bot"""
        return {
            'features': {
                'ai_chat': True,
                'file_processing': True,
                'user_management': True,
                'analytics': True,
                'admin_panel': True,
                'welcome_message': True,
                'smart_responses': True,
                'photo_handling': False,
                'document_handling': False,
            },
            'messages': {
                'welcome': "🤖 Welcome to our community! Please read the rules and enjoy your stay!",
                'help': "📚 Community guidelines and commands are available with /help",
            }
        }
    
    @staticmethod
    def simple_bot():
        """Configuration for simple/basic bot"""
        return {
            'features': {
                'ai_chat': False,
                'file_processing': False,
                'user_management': False,
                'analytics': False,
                'admin_panel': True,
                'welcome_message': True,
                'smart_responses': True,
                'photo_handling': False,
                'document_handling': False,
            },
            'messages': {
                'welcome': "🤖 Hello! I'm your simple assistant bot!",
                'help': "📚 Available commands: /start /help /about",
            }
        }

# Environment validation
def check_environment():
    """Check if all required environment variables are set"""
    required_vars = ['TELEGRAM_BOT_TOKEN']
    missing_vars = []
    
    for var in required_vars:
        if var not in os.environ:
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        print("Please set these variables before running the bot.")
        return False
    
    print("✅ All required environment variables are set!")
    return True

if __name__ == "__main__":
    # Validate configuration
    validation = BotConfig.validate_config()
    print("Configuration Validation:")
    for key, value in validation.items():
        status = "✅" if value else "❌"
        print(f"{status} {key.replace('_', ' ').title()}: {value}")
    
    # Check environment
    check_environment()