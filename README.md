# AutoGitRepo (Git API)
# Requirements
- pip
- virtualenv

# Features
- Buat Repository
- Clone Repository ke Cureent Directory

# Important Notes
- Repository akan diclone menggunakan ssh_url, pastikan anda konek ke github dengan ssh
- Repository akan diclone pada current directory ketika perintah di eksekusi, misal: Anda sedang berada pada `/home/user/mydir/` repo akan di clone pada `/home/user/mydir/repo_name`
- File `create` adalah script bash yang digunakan untuk melakukan eksekusi perintah python (Linux), pastikan anda melakukan update pada pathnya
- Pada Ubuntu Linux, letakkan file create pada `/usr/local/bin/` atau folder program executable yang anda inginkan dengan permission root

# Step By Step
- Clone repo ini `git clone https://github.com/AchmadGozali8/AutoGitRepo`
- Masuk ke directory yang telah di clone `cd AutoGitRepo`
- Setup virtualenv dengan perintah `virtualenv env`
- Install library yang dibutuhkan `pip install -r requirements.txt`
- Pindahkan file create ke folder executable mis: `sudo mv create /usr/local/bin`
- Ganti permission file create, `sudo chown root:root /usr/local/bin/create && sudo chmod +x /usr/local/bin/create`
- Eksekusi perintah dengan `create <nama_repository>`
- Done
