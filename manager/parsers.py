import re


def parse_status(output):

    start_line = None
    end_line = None
    for i, line in enumerate(output):
        if line.startswith('-----'):
            start_line = i + 1
        elif line.strip() == '':
            end_line = i
            break

    status = []
    for line in output[start_line:end_line]:
        match = re.match(
            r'([a-z0-9]+)\s+([a-z0-9A-Z_]+)\s+[a-z]+\s+([a-z]+)\s+([A-Za-z0-9_/]+)',
            line)
        if match:
            status.append({'id': match.group(1),
                           'name': match.group(2),
                           'state': match.group(3),
                           'directory': match.group(4)})

    return status
