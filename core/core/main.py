import qrcode
import os


class Github():
    """
    Create qrcodes for the repositories.
    """
    def __init__(self, folder_name="QRcodes"):
        self.folder_name = folder_name

        if folder_name not in os.listdir():
            os.mkdir(f'./{folder_name}')

    def creator_repository(self, user, repositories):
        for repository in repositories:
            qr = qrcode.make(
                f'https://github.com/{user}/{repository}'
            )
            qr.save(f"{self.folder_name}/{repository}.png")


if __name__ == "__main__":
    github_repositories = [
            "Qrcode_Generator_Python",
            "EmailAutomation_Python",
            "FilesGenerator_Python",
            "PasswordGenerator_Python",
            "CryptoWorksheet_Python",
            "CryptocurrencyQuotes_Python",
        ]
    github = Github()
    github.creator_repository(
        user="SamuelBarbosaDev",
        repositories=github_repositories,
    )
