# Real-World CTF Exercise: HackyCorp

In this series of practical exercises, we will analyze the security vulnerabilities of the website **[https://hackycorp.com](https://hackycorp.com)** and its associated GitHub repositories. Each exercise is a standalone CTF (Capture The Flag) challenge, where the goal is to obtain a flag (`flag`) through research, technical knowledge, and understanding of cybersecurity.

For each challenge, find the **flag** and enter it as proof of successful completion.

---

## Vulnerability Discovery from Known URLs

Sometimes websites use default URLs for login /login /admin, etc. These can reveal certain vulnerabilities and allow for additional information collection.

<details>
<summary>Click here to see the solution</summary>

Let's check the url /admin
Solution flag: `ad1d44d6-ab73-4640-8291-c5bf2343e2a5`
</details>

Hint try to find some more flags in the URL files of static files (images, scripts, etc.).

## Vulnerability detection from public files

The website developers left a public file on the website that contains our key/flag that we are looking for. We are looking for the public key.txt file, which is most likely public (perhaps by mistake), and is located in the same place where the server serves static files (assets), such as images, CSS or JS files.

### Hint / Solution

Hint: in the source code of the website, find the subdomain used to serve static files, then identify the final server using the dig command to gain access to the CDN.
<details>
<summary>Click here to view solution</summary>

The public file is located on the domain in the root folder. The file name is key.txt.
Solution flag: `aeaee57f-2a82-41da-bc4c-d081c8cddfc8`
</details>

## Detecting vulnerabilities in Javascript files

In the next step, we will analyze the website and look for a hardcoded (pre-entered) key among its JavaScript files. Such errors often occur in real applications and can pose a serious security risk, as they allow attackers to access internal systems or data.

### Hint / Solution

Hint: find the script used in the website source code, then find the key.

<details>
<summary>Click here to view solution</summary>
We search the JS files, in one of them we find a record of the key.
Solution Flag: `d6b75269-97a3-44de-be32-fff0dd55e7ef`
</details>

## Web Server Vulnerability Detection

Sometimes a web server exposes certain information in the request header. One example is using a curl request to a domain or examining a robots.txt file.

<details>
<summary>Click here to view the solution</summary>

curl -I https://hackycorp.com/
Solution flag: `99d0738b-1e52-4a00-8885-b15894b2c79e`

curl https://hackycorp.com/robots.txt
Solution flag: `af9c328a-02b4-439d-91c6-f46ab4a0835b`

</details>

The SSL server usually creates a security.txt file for the certificate, which can also reveal certain information.

<details>
<summary>Click here to view the solution</summary>

curl https://hackycorp.com/.well-known/security.txt
Solution flag: `99685e30-7061-4ac0-83bf-4ccc0409faac`

</details>

We can also try curl requesting a non-existent page - 404 error.

<details>
<summary>Click here to view the solution</summary>

curl -I https://hackycorp.com/doesn't exist
Solution flag: `99d0738b-1e52-4a00-8885-b15894b2c79e`

</details>

## Vulnerability detection via IP address

A domain's root IP server can serve a separate web server and potentially reveal certain information.

<details>
<summary>Click here to view the solution</summary>

curl --insecure http://HOST_IP
Solution flag: `5cf83b5d-eb6c-4eee-af6c-945f9aed8dfd`

</details>

## Vulnerability detection in Github repositories

In this task, we will explore the GitHub repository, where we will check all existing branches and try to find hidden or sensitive data that is not in the default (main or master) branch. For Github exercises, we will use the organization profile: https://github.com/hackycorp

### Vulnerability detection in repo3

Hint: Explore the project branches in the repo3 repository.

<details>
<summary>Click here to view the solution</summary>
In repo3, we find a branch that contains the flag.
Solution flag: `08be82ba-e5fd-4fae-b2c2-272a18d31f80`
</details>

### Vulnerability detection in repo4

We do the same for the repo4 repository.

<details>
<summary>Click here to view the solution</summary>
This time the flag is located in a file in a different branch.
Solution flag: `a60b4aee-642a-483b-9262-ccfc2ed46f0d`
</details>

### Vulnerability detection in repo9

Next, let's focus on repo9. Here we need to look for changes in the files where we find the deleted key.

<details>
<summary>Click here to view the solution</summary>
Let's find the changes
git log --diff-filter=D --summary &&
git log -- KEY.txt &&
git show COMMIT_HASH:KEY.txt
Solution flag: `3ee505c2-8aa9-4d5e-810e-921778dce1e6`
</details>

### Vulnerability detection in repo0a

Next, let's focus on repo0a. Here we need to find the message sent with the write, where we find the written key.

<details>
<summary>Click here to view the solution</summary>
Let's find the log
git log --oneline &&
git log --oneline --grep=key -i &&
git show COMMIT_HASH
Solution flag: `5c75cfe9-52dd-475b-8cfa-7ffc492abeca`
</details>

Try to find the keys in the repositories:
- https://github.com/hackycorp/repo1
- https://github.com/hackycorp/repo7
- https://github.com/hackycorpdev/test1

## Detecting vulnerabilities in DNS records

Sometimes, by examining TXT records, we can obtain information that includes sensitive data. An example of this can be obtained by examining the TXT record of the domain key.z.hackycorp.com.

<details>
<summary>Click here to view the solution</summary>
Hint: dig key.z.hackycorp.com TXT

You could also use a bruteforce strategy:
```bash
for sub in key test dev txt api admin; do
dig $sub.z.hackycorp.com TXT +short
done
```
Solution flag: `9f883f22-6ea5-4631-bbe8-95841ad63f56`
</details>

## Using the DNS record synchronization mechanism

In this task, we will perform a DNS synchronization on the z.hackycorp.com domain zone and thus try to obtain a list of DNS records that the server exposes.
Note: only works in a virtualized environment

We use:
dig AXFR z.hackycorp.com
dig -t SOA z.hackycorp.com
dig AXFR z.hackycorp.com @z.hackycorp.com

<details>
<summary>Click here to view solution</summary>

Solution flag: `e5fce970-6d94-43c1-bdd5-a06c2b235f9c`
</details>

## Disclosing information using software queries

The version of the software being used often reveals potential security vulnerabilities.

Note: only works in a virtualized environment

We use:
dig -c chaos -t txt VERSION.BIND @z.hackycorp.com

<details>
<summary>Click here to view the solution</summary>

Solution flag: `4e5e76e1-728a-49be-aea8-4591ba11e588`
</details>

## Scripting and automation

We can often help by preparing a script that uses a brute-force strategy to perform certain actions.

We will prepare two scripts:

```bash
for i in `seq 1 150`
do
printf "0x%02x.a.hackycorp.com\n" $i >> hosts.txt
done
```

```bash
for i in `cat hosts.txt`
do
curl $i/logo.png -o $i.png
done
```

You can also try other CTF challenges on the following websites:
- https://www.root-me.org/
- https://pentesterlab.com/exercises/
- https://tryhackme.com/hacktivities