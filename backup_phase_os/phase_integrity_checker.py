"""Phase OS Module Integrity Checker
Verifies that phase configuration files exist and that phase modules import without error.
"""

import importlib
import json
import os
import sys

PHASES_FILE = './phases.json'
TRIGGERS_FILE = './phase_triggers.json'


def check_phases():
    if not os.path.exists(PHASES_FILE):
        print(f'❌ Missing {PHASES_FILE}')
        return None
    with open(PHASES_FILE) as f:
        data = json.load(f)
    phases = data.get('phases')
    if not isinstance(phases, dict):
        print('❌ phases.json missing "phases" key')
        return None
    print(f'✅ Loaded {len(phases)} phases from {PHASES_FILE}')
    return phases


def check_triggers(phases):
    if not os.path.exists(TRIGGERS_FILE):
        print(f'⚠️  {TRIGGERS_FILE} not found')
        return
    with open(TRIGGERS_FILE) as f:
        trig = json.load(f)
    missing = [info["name"] for info in phases.values() if info["name"] not in trig]
    if missing:
        print(f'⚠️  No triggers defined for: {", ".join(missing)}')
    else:
        print('✅ All phases have trigger definitions')


def check_modules(prefix='phase_'):
    failures = []
    for fname in os.listdir('.'):
        if fname.startswith(prefix) and fname.endswith('.py'):
            mod_name = fname[:-3]
            try:
                importlib.import_module(mod_name)
            except Exception as e:
                failures.append((mod_name, str(e)))

    if failures:
        print('⚠️  Module import issues detected:')
        for mod, err in failures:
            print(f'   {mod}: {err}')
    else:
        print('✅ All phase modules imported successfully')


def main():
    phases = check_phases()
    if phases is None:
        sys.exit(1)
    check_triggers(phases)
    check_modules()


if __name__ == '__main__':
    main()

