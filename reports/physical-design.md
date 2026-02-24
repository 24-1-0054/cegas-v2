# Physical Design

As only one person can use the server at once, implementing concurrency is not 
needed. No two database interfaces will be simultaneously running, which means 
low memory and CPU requirements. Disk space will be reserved solely for the 
database, made mostly of files in the megabytes to low-gigabytes range, 
meaning an old 64 GB Hard Disk Drive (HDD) would be more than enough in terms 
of speed and space. Backups will be done daily within the server externally 
via USB drives.

However, even with low hardware requirements. We still recommend more recent 
hardware (at least 5 years) for ease of maintenance (It Foundations, 2023).

Debian 13 was chosen as an operating system due to its low 
hardware requirements (Debian, 2024), up-to-date repositories via `apt`, 
and widespread support. 

## Notable software
###  Official hardware requirements (Debian, 2024)
| Install Type | RAM (minimum) | RAM (recommended) | Hard Drive
|:-------------|:-------------:|:-----------------:|-------------:|
| No desktop   | 256 megabytes | 512 megabytes     | 4 gigabytes  |
| With desktop | 1 gigabyte    | 2 gigabytes       | 10 gigabytes |

### Database software
The CEGAS depends on the following Python + pip v3.14  (current latest)

The following will likely be used for security/administration. These are only
for consideration and will only be fully decided at the implementation stage:
- Full Disk Encryption (FDE) software (e.g. LUKS/VeraCrypt)
- USBGuard (USB flash drive whitelisting/blacklisting package)

## Hardware Recommendations

Specs can go lower or higher, these are general recommendations.
Any laptop or desktop with these specs: 

1. Disk: 64 GB USB Flash Drive (SSD) (x3)
    - These come cheap, less than P1000 on average in local stores.
    - One is more than enough for the entire database, others are for backups.
    - ~100 read/write speeds should be enough to run all 
    database systems at an unnoticeable speed.
2. RAM: 8 GB DDR3
    - DDR3 is fast enough and is still manufactured.
    - 2x 4 GB sticks are more than enough and are still manufactured.
3. CPU: any `amd64` CPU made within the last 5 years
    - Hard to make a specific recommendation, the above is a rule of thumb.