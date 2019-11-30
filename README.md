# AutoGitRepo (Git API)
# Requirements
- pip
- virtualenv
- python 2.7

# Features
- Buat Repository
- Clone Repository ke Current Directory

# Important Notes
- Pastikan anda memiliki token github jika belum, anda dapat mengenerate pada halaman berikut https://github.com/settings/tokens
- Masukkan token yang telah digenerate pada file main.py di variable TOKEN
- Repository akan diclone menggunakan ssh_url, pastikan anda konek ke github dengan ssh
- Repository akan diclone pada current directory setelah perintah di eksekusi, misal: Anda sedang berada pada `/home/user/mydir/` repo akan di clone pada `/home/user/mydir/repo_name`
- File `create` adalah script bash yang digunakan untuk melakukan eksekusi perintah python (Unix), pastikan anda melakukan update pada pathnya
- [Unix] Letakkan file create pada `/usr/local/bin/` atau folder program executable yang anda inginkan

# Step By Step
- Clone repo ini `git clone https://github.com/AchmadGozali8/AutoGitRepo`
- Masuk ke directory yang telah di clone `cd AutoGitRepo`
- Setup virtualenv dengan perintah `virtualenv env`
- Install library yang dibutuhkan `pip install -r requirements.txt`
- Pindahkan file create ke folder executable mis: `sudo mv create /usr/local/bin`
- Eksekusi perintah dengan `create -h` untuk menampilkan semua options.
- Contoh penggunaan: `create -n instagram_clone -p -g Dart` ( jika dibahasa manuasiakan: buat repo instagram_clone atur sebagai private dan tambahkan template .gitignore Dart setelah itu clone pada current directory )
  - `-n` => Name
  - `-p` => Private
  - `-g` => .gitignore template
  
- Done
