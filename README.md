# Github-Actions-with-schedule-task

Here's a README.md for the GitHub project that outlines how to set up, run, and manage the project:

---

# Fetch Data Scheduled Task

This project uses GitHub Actions to run a Python script that fetches data from an API at 15:30 IST, Monday to Friday. The data is saved in a directory structure based on the current date. 

## Features

- Scheduled task using GitHub Actions
- Secure handling of sensitive information using GitHub secrets
- Directory structure based on the current date
- Automatic commit and push of fetched data to the repository

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/your-username/fetch-data-scheduled-task.git
   cd fetch-data-scheduled-task
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.github/workflows` directory** (if not already present) and add the workflow file:

   ```yaml
   # .github/workflows/fetch_data.yml
   name: Fetch Data

   on:
     schedule:
       - cron: '00 10 * * 1-5'  # 15:30 IST is 10:00 UTC

   jobs:
     fetch_data_job:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout repository
         uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.x'

       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install requests

       - name: Run fetch_data script
         env:
           USERNAME: ${{ secrets.USERNAME }}
           PASSWORD: ${{ secrets.PASSWORD }}
           ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
           API_KEY: ${{ secrets.API_KEY }}
         run: python fetch_data.py

       - name: Commit and push changes
         run: |
           git config --global user.name 'github-actions[bot]'
           git config --global user.email 'github-actions[bot]@users.noreply.github.com'
           git add Data/
           git commit -m 'Add fetched data'
           git push
         env:
           GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
   ```

## Secrets

Add the following secrets to your GitHub repository:

1. Go to `Settings` > `Secrets and variables` > `Actions` > `New repository secret`.
2. Add the following secrets:
   - `USERNAME`
   - `PASSWORD`
   - `ACCESS_TOKEN`
   - `API_KEY`
   - `GITHUB_TOKEN` (already available in GitHub Actions)

## Usage

1. **Run the script locally (for testing)**

   ```sh
   python fetch_data.py
   ```

2. **Push changes to GitHub**

   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

The GitHub Actions workflow will automatically run at the scheduled time (15:30 IST, Monday to Friday) and fetch data from the API, saving it in the directory structure based on the current date.

## Best Practices

- **Use Environments**: Utilize GitHub environments for different deployment stages (e.g., development, staging, production).
- **Monitor Workflows**: Regularly check the Actions tab for workflow run status and logs.
- **Notifications**: Set up notifications for workflow failures to quickly address issues.
- **Security**: Regularly rotate secrets and limit access to sensitive data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

This README provides a concise and clear guide for setting up and running the project, while also highlighting best practices for managing and using GitHub Actions.
