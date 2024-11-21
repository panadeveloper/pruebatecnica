class SecondaryDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'factura':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'factura':
            return 'secondary'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'factura':
            return db == 'secondary'
        return db == 'default'

