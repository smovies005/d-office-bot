class script(object):  
    START_TXT = """<b>✨ Hᴇʟʟᴏ {user}.

Mʏ Nᴀᴍᴇ Is {bot}.

<p style="font-size: 20px; font-weight: bold;">🎬 I Can Provide Movies For You! 🍿</p>

<p>Just add me to your group or join our group to enjoy a wide selection of movies!</p> """
    
    HELP_TXT = "Hᴇʏ {}\nHᴇʀᴇ Mꜱ Mʏ Hᴇʟᴩ"

    ABOUT_TXT = """<b>✯ My Name : {}

    <b><i>• Movie/Series request format :-</i></b>

    <b>  Example Movie:</b>
    Bhul bhulaiya full movie Hindi 720p❌
    My fault full movie ❌
    My fault 2023 ✅
    My fault ✅
    My fault 2023 ✅

    <b> Example Web Series:</b>
    Loki Season 01 2022 full season ❌
    Loki Season 01 2022 ❌
    Loki S1 ✅
    Loki S01E01 ✅

• Spelling Should Be Right, Otherwise Not Relpy
     
     """
   
    FILE_TXT = """<b>✨ File Store Help ✨</b>

<i>Store your files forever with our File Store module! 🗄️</i>

<b>Features:</b>

🔒 Store files securely in our database.
🌐 Get permanent links to access your files anytime, anywhere.
📁 Add files from public channels by simply sending the file link.
🤫 Add files from private channels by making me an admin on the channel.

<b>Commands:</b>

🔗 Link: Reply to any media to get a permanent link.
🔗 Batch: Send multiple file links, separated by spaces, to get links for all the files.

<b>Examples:</b>

✨ Reply to a file with Link to get a permanent link to the file.
✨ Send multiple file links, separated by spaces, with Batch to get links for all the files.

</code>/batch https://t.me/Doffice_bots/1 https://t.me/Doffice_bots/10</code>"""
  
    FILTER_TXT = "Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨"
    
    GLOBALFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>


<p style="font-size: 20px; font-weight: bold;">✨ Filter 🌟</p>

<p>The Filter feature allows users to set up automated replies for specific keywords. Whenever a keyword is found in a message, the bot will automatically respond with the corresponding reply.</p>

<p style="font-size: 16px;">📝 Note: 📝</p>

<p>This module is only accessible to my admins.</p>

<p style="font-weight: bold;">Commands & Usage:</p>

<ul>
<li>/gfilter: Add global filters.</li>
<li>/gfilters: View a list of all global filters.</li>
<li>/delg: Delete a specific global filter.</li>
<li>/delallg: Delete all global filters.</li>
</ul>

<p>/g_filter off or /g_filter on: Enable or disable global filters in your group.</p>

"""

    MANUELFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Fɪʟᴛᴇʀs</b>

<p style="font-size: 20px; font-weight: bold;">✨ Filter 🌟</p>

<p>The Filter feature allows users to set up automated replies for specific keywords. Whenever a keyword is found in a message, the bot will automatically respond with the corresponding reply.</p>

<p style="font-size: 16px;">📝 Note: 📝</p>

<ol>
<li>This bot should have admin privileges.</li>
<li>Only admins can add filters in a chat.</li>
<li>Alert buttons have a limit of 64 characters.</li>
</ol>

<p style="font-weight: bold;">Commands & Usage:</p>

<ul>
<li>/filter: Add a filter in chat.</li>
<li>/filters: List all the filters of a chat.</li>
<li>/del: Delete a specific filter in chat.</li>
<li>/delall: Delete the whole filters in a chat (chat owner only).</li>
</ul>

<p>/g_filter off: Use this command + on/off in your group to control global filter in your group.</p>
"""

    BUTTON_TXT = """<b>Hᴇʟᴘ Fᴏʀ Bᴜᴛᴛᴏɴs</b>

<p style="font-size: 20px; font-weight: bold;">✨ Button Feature 🌟</p>

<p>This bot supports both URL and alert inline buttons.</p>

<p style="font-size: 16px;">📝 Note: 📝</p>

<ol>
<li>Telegram will not allow you to send buttons without any content, so content is mandatory.</li>
<li>This bot supports buttons with any Telegram media type.</li>
<li>Buttons should be properly parsed as Markdown format.</li>
</ol>

<p style="font-weight: bold;">URL Buttons:</p>

<pre>
[Button Text](buttonurl:xxxxxxxxxxxx)
</pre>

<p style="font-weight: bold;">Alert Buttons:</p>

<pre>
[Button Text](buttonalert:This Is An Alert Message)
</pre>
"""

    AUTOFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ AᴜᴛᴏFɪʟᴛᴇʀ</b>
<p style="font-size: 20px; font-weight: bold;">🌟 Auto Filter 🌟</p>

<p>The Auto Filter feature allows you to automatically filter and save files from a channel to a group. You can use the following commands to enable/disable Auto Filter in your group:</p>

<ul>
<li>/autofilter on: Enable Auto Filter in your chat</li>
<li>/autofilter off: Disable Auto Filter in your chat</li>
</ul>

<p style="font-weight: bold;">Other Commands:</p>

<ul>
<li>/set_template: Set the IMDb template for your group</li>
<li>/get_template: Get the current IMDb template for your group</li>
</ul>
"""

    CONNECTION_TXT = """<b>Hᴇʟᴘ Fᴏʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b>

<p style="font-size: 20px; font-weight: bold;">✨ Connect to PM ✨</p>

<p>Use this feature to connect the bot to your PM for managing filters. This helps to avoid spamming in groups.</p>

<p style="font-size: 16px;">📝 Note: 📝</p>

<ul>
<li>Only admins can add a connection.</li>
<li>Send `/connect` for connecting me to your PM.</li>
</ul>

<p style="font-weight: bold;">Commands & Usage:</p>

<ul>
<li>/connect: Connect a particular chat to your PM.</li>
<li>/disconnect: Disconnect from a chat.</li>
<li>/connections: List all your connections.</li>
</ul>
"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>
    
<p style="font-size: 20px; font-weight: bold;">✨ Admin Module ✨</p>

<p style="font-weight: bold;">Commands & Usage</p>

<ul>
    <li>/logs: Get the recent errors.</li>
    <li>/delete: Delete a specific file from the database.</li>
    <li>/deleteall: Delete all files from the database.</li>
    <li>/users: Get a list of my users and IDs.</li>
    <li>/chats: Get a list of my chats and IDs.</li>
    <li>/channel: Get a list of total connected channels.</li>
    <li>/broadcast: Broadcast a message to all users.</li>
    <li>/group_broadcast: Broadcast a message to all connected groups.</li>
    <li>/leave: Leave a chat with chat ID.</li>
    <li>/disable: Disable a chat with chat ID.</li>
    <li>/invite: Get the invite link of any chat where the bot is an admin.</li>
    <li>/ban_user: Ban a user with ID.</li>
    <li>/unban_user: Unban a user with ID.</li>
    <li>/restart: Restart the bot.</li>
    <li>/clear_junk: Clear all deleted accounts and blocked accounts in the database.</li>
    <li>/clear_junk_group: Clear added removed groups or deactivated groups on the database.</li>
</ul>
"""


    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code> Only admin</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code> Only admin</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code> Only admin</code>
◉ ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>Only admin </code></b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

<p style="font-size: 20px; font-weight: bold;">🏆 Group Info 🏆</p>

<ul>
<li><b>Group:</b> {a}</li>
<li><b>Group ID:</b> <code>{b}</code></li>
<li><b>Link:</b> @{c}</li>
<li><b>Members:</b> <code>{d}</code></li>
<li><b>Added By:</b> {e}</li>
</ul>

<p style="font-weight: bold;">Information by: @{f}</p>
"""
  
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
<p style="font-size: 20px; font-weight: bold;">👤 User Info 👤</p>

<ul>
<li><b>User ID:</b> <code>{}</code></li>
<li><b>Account Name:</b> {}</li>
<li><b>Username:</b> @{}</li>
</ul>

<p style="font-weight: bold;">Information by: @{}</p>
"""
  
    GROUPMANAGER_TXT = """<b>Hᴇʟᴩ Fᴏʀ GʀᴏᴜᴩMᴀɴᴀɢᴇʀ</b>
<p style="font-size: 20px; font-weight: bold;">✨ Chat Management ✨</p>

<p>This feature is designed to assist you in managing your group. It is accessible only to group administrators.</p>

<p style="font-weight: bold;">Commands & Usage:</p>

<ul>
    <li>/inkick: Command with required arguments, and I will kick members from the group.</li>
    <li>/instatus: Check the current status of chat members from the group.</li>
    <li>/dkick: Kick deleted accounts.</li>
    <li>/ban: Ban a user from the group.</li>
    <li>/unban: Unban a banned user.</li>
    <li>/tban: Temporarily ban a user.</li>
    <li>/mute: Mute a user.</li>
    <li>/unmute: Unmute a muted user.</li>
    <li>/tmute: Mute a user up to a particular time. Eg: `/tmute 2h` to mute for 2 hours. Values are (m/h/d).</li>
    <li>/pin: Pin a message to your chat.</li>
    <li>/unpin: Unpin a message from your chat.</li>
    <li>/purge: Delete all messages from the replied to message to the current message.</li>
</ul>
 """

    EXTRAMOD_TXT = """<b>Hᴇʟᴩ Fᴏʀ Exᴛʀᴀ Mᴏᴅᴜʟᴇ</b>

<p>**Commands & Usage:**</p>

<ul>
    <li>/id: Get ID of a specified user.</li>
    <li>/info: Get information about a user.</li>
    <li>/imdb: Get the film information from IMD source.</li>
</ul>
"""    
    
    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"
      
    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"
      
    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"
      
    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"
      
    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"
      
    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"
      
    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"
   
    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
    Uᴩᴛɪᴍᴇ: {}
    CPU Uꜱᴀɢᴇ: {}%
    RAM Uꜱᴀɢᴇ: {}%
    Tᴏᴛᴀʟ Dɪꜱᴋ: {}
    Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
    Fʀᴇᴇ Dɪꜱᴋ: {}"""
    
    BUTTON_LOCK_TEXT = "Hᴇʏ {query}\nTʜɪꜱ Iꜱ Nᴏᴛ Fᴏʀ Yᴏᴜ. Sᴇᴀʀᴄʜ Yᴏᴜʀ Sᴇʟꜰ"
   
    FORCE_SUB_TEXT = "Sᴏʀʀʏ Bʀᴏ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Cʟɪᴄᴋ Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"
   
    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ"""
  
    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ: {query}</b>

🏷 Tɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 Gᴇɴʀᴇꜱ: {genres}
📆 Yᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 Rᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a>/10"""
   
  
 


   
  
 


