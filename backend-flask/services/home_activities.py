from datetime import datetime, timedelta, timezone
class HomeActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [
      {  
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eeg',
        'profile_picture': '/bubble w02.png',
        'handle': 'Cruddur Campbot 02',
        'message': 'Week 02 - Distributed Tracing with Honeycomb',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 2,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea69',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eeg',
          'profile_picture': '/logo_mariachi_in_a_jar_white.png',
          'handle':  'Mariachi in a Jar',
          'message': 'Week 02 Sunday - Something went wrong with the Frontend. Doing this task all over again!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
      }, 
      {
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea70',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
        'profile_picture': '/logo_mariachi_in_a_jar_white.png',
        'handle':  'Mariachi in a Jar',
        'message': 'Week 02 Monday morning 3 AM - sidetracked from notification feature because frontend is so much fun! lol. Updated homefeed page and Desktop Sidebar feature!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
      },
      {
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
        'profile_picture': '/bubble w01.png',
        'handle': 'Cruddur Campbot 01',
        'message': 'Week 01 - Create the notification feature (Backend and Front)',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 2,
        'reposts_count': 0,
        'replies': [
          {
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea65',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
            'profile_picture': '/logo_mariachi_in_a_jar_white.png',
            'handle':  'Mariachi in a Jar',
            'message': '✅ *DynamoDB and Postgres vs Docker*: Created Music table, furnished it with my fav songs! [Week 02 Wednesday]',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }, 
          {
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
            'profile_picture': '/logo_mariachi_in_a_jar_white.png',
            'handle':  'Mariachi in a Jar',
            'message': '✅ Write a Flask Backend Endpoint for Notifications - Something went wrong with the Frontend. Doing this task all over again! [Week 02 Sunday]',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }, 
          {
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea69',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
            'profile_picture': '/logo_mariachi_in_a_jar_white.png',
            'handle':  'Mariachi in a Jar',
            'message': '🔍 Sidetracked from notification feature because frontend is so much fun! lol. Updated homefeed page and Desktop Sidebar feature! [Week 02 Monday morning 3 AM]',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }],
      },
      {
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eea',
        'profile_picture': '/bubble w00.png',
        'handle': 'Cruddur Campbot 00',
        'message': 'Week 00 - Architecture and Billing',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 2,
        'reposts_count': 0,
        'replies': 
        [
          {
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea66',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eea',
            'profile_picture': '/logo_mariachi_in_a_jar_white.png',
            'handle':  'Mariachi in a Jar',
            'message': 'Week 02 Sunday - Something went wrong with the Frontend. Doing this task all over again!',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }, 
          {
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea69',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eef',
            'profile_picture': '/logo_mariachi_in_a_jar_white.png',
            'handle':  'Mariachi in a Jar',
            'message': 'Week 02 Monday morning 3 AM - sidetracked from notification feature because frontend is so much fun! lol. Updated homefeed page and Desktop Sidebar feature!',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }
        ],
      },
      {
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'profile_picture': '/logo_matryoshka_in_the_cloud.png',
        'handle':  'Matryoshka in the Cloud',
        'message': 'Всем привет! Я хочу изучить Cloud.',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 2,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'profile_picture': '/logo_matryoshka_in_the_cloud.png',
          'handle':  'Matryoshka in the Cloud',
          'message': 'Я не поддерживаю войну.',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat(),
          'replies': [{
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea66',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Matryoshka in the Cloud',
            'profile_picture': '/logo_matryoshka_in_the_cloud.png',
            'message': 'Слава Україні!',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
          }],
        }],
      },
      {
        'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
        'handle':  'Worf',
        'message': 'I am out of prune juice',
        'created_at': (now - timedelta(days=7)).isoformat(),
        'expires_at': (now + timedelta(days=9)).isoformat(),
        'likes': 0,
        'replies': []
      },
      {
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Garek',
        'message': 'My dear doctor, I am just simple tailor',
        'created_at': (now - timedelta(hours=1)).isoformat(),
        'expires_at': (now + timedelta(hours=12)).isoformat(),
        'likes': 0,
        'replies': []
      }
    ]
    return results