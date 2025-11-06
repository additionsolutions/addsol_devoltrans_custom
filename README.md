### Addsol Devoltrans Custom

Customizations done for DeVoltrans implementation

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app addsol_devoltrans_custom
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/addsol_devoltrans_custom
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade


### Run this commands to reload
(replace 'deverp.aitspl.com' with site name)

bench --site deverp.aitspl.com clear-cache
// bench --site deverp.aitspl.com reload-doc addsol_devoltrans_custom

bench restart

If restart gives error, try:
bench setup socketio
bench setup supervisor
bench setup redis
sudo supervisorctl reload

### Confirm if hooks are merged
bench --site deverp.aitspl.com execute frappe.get_hooks --args doc_events
bench --site deverp.aitspl.com execute frappe.get_hooks --args scheduler_events
bench --site deverp.aitspl.com execute frappe.get_hooks --args override_whitelisted_methods
