To obtain your **GOOGLE_CLIENT_ID**, **GOOGLE_CLIENT_SECRET**, and set your **GOOGLE_REDIRECT_URI** for Google OAuth integration, follow these official steps:

### **How to Get GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET**

1. **Go to the Google Cloud Console:**
   - Visit: [Google Cloud Console](https://console.cloud.google.com/)

2. **Create a new project (or select an existing one):**
   - Click the project drop-down at the top.
   - Click "New Project", enter a name, and create it[1][2].

3. **Configure OAuth Consent Screen:**
   - In the left menu, go to **APIs & Services → OAuth consent screen**.
   - Choose "External" or "Internal".
   - Fill in the application information (name, email, authorized domains, etc.) and save.

4. **Create OAuth Credentials:**
   - In the left menu, go to **APIs & Services → Credentials**.
   - Click **"Create Credentials" → "OAuth client ID"**.
   - For **Application type**, select **Web application**.

5. **Set Authorized Redirect URIs:**
   - In the setup form, fill in a name for your OAuth client.
   - Under **Authorized redirect URIs**, add the URL where your backend will handle Google’s response (see below).

6. **Save and Retrieve Your Credentials:**
   - Click "Create".
   - You’ll see a dialog or JSON file with your **Client ID** and **Client Secret**. Copy these—they are your `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`.
   - You can view or download them later under "OAuth 2.0 Client IDs" in the Credentials section[1][2][3].

### **What is GOOGLE_REDIRECT_URI? How do I set it?**

- The `GOOGLE_REDIRECT_URI` is the **URL in your backend where Google will redirect after user authentication**.
- It must exactly match the value you add in the "Authorized redirect URIs" in the Google console.
- Typical local development value:  
  ```
  http://localhost:8000/api/v1/auth/google-callback
  ```
- For production, use your live backend URL, e.g.:  
  ```
  https://yourdomain.com/api/v1/auth/google-callback
  ```

### **In Summary**

- Get `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` from the Google Cloud Console → APIs & Services → Credentials → Create OAuth Client ID.
- Set `GOOGLE_REDIRECT_URI` to your backend’s Google callback handler, and **use the exact same URI in both your backend code and in the Google Cloud Console's "Authorized redirect URIs"**.
- Save these values in your `.env` or settings file and reference them in your app.

Here’s detailed guidance based on your message about the Google OAuth client ID, test users, and access restrictions:

===================================================================

## 1. **Where to Find Your Client ID**

- **Google OAuth client IDs** are accessed from the **Clients** tab under the Google Auth Platform section in the [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
- Each OAuth client ID uniquely identifies a single app (web, Android/iOS, etc.) to Google's authorization servers[1].

## 2. **OAuth Access Is Restricted to Test Users While in Testing Mode**

- **If your app’s Publishing status is "Testing"** (the default for new OAuth apps), **only the emails listed as “test users” on your OAuth consent screen can authorize with Google**[2][3][4][5].
- **Test Users list:**  
  - Manage by going to **APIs & Services → OAuth consent screen → Test users**  
  - You can add your own Google account and any collaborators.
  - Up to 100 test users are supported per project in Testing mode[4].

## 3. **What Happens for Unlisted Users?**

- Anyone **not** on the test user list **will be blocked** from authenticating with your app while it’s in "Testing" mode.
- Only users in the test user list can get OAuth tokens via your app during testing[2][6].
- If you want to allow all users, you’ll need to publish your app and possibly pass Google verification if you use sensitive or restricted scopes.

## 4. **Useful Links and Next Steps**

- **Add or manage test users:**  
  [Google Cloud Console OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)
- **How to add test users:**  
  *In the Cloud Console → APIs & Services → OAuth consent screen → Audience → Test users → Add users → Enter email address(es) → Save*[2][3][5].
- **Official Google Guide:**  
  [Configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent)[2]

### Summary Table

| Step                         | Where/How                                                                            |
|------------------------------|--------------------------------------------------------------------------------------|
| Find Client ID               | Cloud Console → APIs & Services → Credentials → OAuth 2.0 Client IDs                 |
| Restrict to test users       | Cloud Console → APIs & Services → OAuth consent screen → Audience → Test users       |
| Add/Change test users        | Click "Add users", enter Google email addresses, then save                           |
| Access blocked for others    | Only test users will be able to authorize during "Testing" status                    |
| Publish for all users        | Complete Google verification, then change status to "Production" if going public     |

**In short:**  
Your **Client ID** uniquely identifies your app.  
While in testing, **only “test users”** added on the consent screen can log in with Google OAuth via your app.  
You can always review and edit this list from the consent screen’s Audience tab[2][3][5].  
If you want to open up access to everyone, you must publish the app and (if required) complete the verification process.
