""" migracion"""
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """class migracion"""
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='Chatbot Cabanas', max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cabanas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('capacidad', models.PositiveIntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
                ('chatbot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cabanas', to='django_local.chatbot')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('DNI', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('chatbot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientes', to='django_local.chatbot')),
            ],
        ),
        migrations.CreateModel(
            name='Alquileres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('capacidad_cabanas', models.PositiveIntegerField()),
                ('cantidad_clientes', models.PositiveIntegerField()),
                ('Cabanas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alquileres', to='django_local.cabanas')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alquileres', to='django_local.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagada', models.BooleanField(default=True)),
                ('alquileres', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='factura_alquiler', to='django_local.alquileres')),
                ('chatbot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facturas', to='django_local.chatbot')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], max_length=20)),
                ('chatbot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagos', to='django_local.chatbot')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='django_local.factura')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('capacidad_cabanas', models.PositiveIntegerField()),
                ('cantidad_clientes', models.PositiveIntegerField()),
                ('Cabanas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='django_local.cabanas')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='django_local.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroDiario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('alquileres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='django_local.alquileres')),
                ('Cabanas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='django_local.cabanas')),
                ('chatbot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros', to='django_local.chatbot')),
                ('reservas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='django_local.reserva')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='reserva',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='django_local.reserva'),
        ),
    ]
