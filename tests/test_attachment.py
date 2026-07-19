import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from codal_attachment import CodalAttachment


x = CodalAttachment(
    "OOObOOOaNGDL045HqC0wNGueH5Hw=="
)

data = x.get_attachments()

open(
    "attachment_result",
    "wb"
).write(data)