import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5603607413:AAF9jqPDuGeMBcdlhxhV6RLyJyGmFGrPaL8"
    APP_ID = 16193102
    API_HASH = "75eadea6904c83b9be6f2114bd45f6ff"
    TG_USER_SESSION = "AQAiEMB34z_0wZxomC_TQfaLiKgPltoFt8Oio9fYQo2GLgu58Jv5w7EqTm_FE4tQgRtuYVk23uBVwMYXH5ovPfs2A2UpUvwsSfXaNGfNoG0Kk8X3yaRwNMFd1OjbAFLzMwlyTv-U175uadOC-g_T89Nq7Tad_G7sT8LPGGYILdk5MyKSKAXecgBm9PFa0m_T798hAlcPcWaeOkmmldYc801vvCGVSR-UE81Z6Mj2Q9m3s76vnR0ZioO5ds_fimQRIkndELWpOtJa0OBl74v_eCUkWbEI1n-jnWDDmA56NWqrXyw_n3g1_nyPsq5rnfVHZlh0DxNnA6eT7J7qWbhojf-2aqqijAA"
    DB_URI = "postgres://user:4uNJdS24TCQoDggrftafPPQEoao4A99F@dpg-cefhquh4reb3r0pvkqq0-a/clonebot"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
