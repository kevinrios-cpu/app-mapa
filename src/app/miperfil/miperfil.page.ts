import { Component, OnInit } from '@angular/core';
import {
  FormGroup,
  FormControl,
  Validators,
  FormBuilder
} from '@angular/forms'
import { AlertController, NavController } from '@ionic/angular';

@Component({
  selector: 'app-miperfil',
  templateUrl: './miperfil.page.html',
  styleUrls: ['./miperfil.page.scss'],
})
export class MiperfilPage implements OnInit {

  formularioPerfil: FormGroup;

  constructor(public fb: FormBuilder,
    public alertController: AlertController,
    public navCtrl: NavController) {
    this.formularioPerfil = this.fb.group({
      'name': new FormControl("",Validators.required),
      'rut': new FormControl("", Validators.required),
      'password': new FormControl("", Validators.required),
      'patente': new FormControl("",Validators.required),
      'foto': new FormControl("",Validators.required)
    })
   }

  ngOnInit() {
  }

  async guardar(){
    var f = this.formularioPerfil.value;
    if(this.formularioPerfil.invalid){
      const alert = await this.alertController.create({
        header: 'Datos incompletos',
        message: 'Tienes que llenar todos los datos',
        buttons: ['Aceptar']
      });
  
      await alert.present();
      return;
    }
    var usuario = {
      rut: f.rut,
      password: f.password,
      name: f.name,
      patente: f.patente,
      foto: f.foto
    }
    localStorage.setItem('usuario',JSON.stringify(usuario));
  }

}
