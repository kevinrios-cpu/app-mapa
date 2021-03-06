import { Component, OnInit } from '@angular/core';
import {
  FormGroup,
  FormControl,
  Validators,
  FormBuilder
} from '@angular/forms'
import { AlertController, NavController } from '@ionic/angular';
@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  formularioLogin: FormGroup;

  constructor(public fb: FormBuilder,
    public alertController: AlertController,
    public navCtrl: NavController) {

    this.formularioLogin = this.fb.group({
      'rut': new FormControl("",Validators.required),
      'password': new FormControl("",Validators.required)
    })

   }

  ngOnInit() {
  }

  async ingresar(){
    var f = this.formularioLogin.value;

    var usuario = JSON.parse(localStorage.getItem('usuario'));

    if(usuario.rut == f.rut && usuario.password == f.password){
      console.log('Ingresado');
      localStorage.setItem('ingresado','true');
      this.navCtrl.navigateRoot('inicio');
    }
    else{
      const alert = await this.alertController.create({
        header: 'Datos icorrectos',
        message: 'Los datos que ingresaste son incorrectos',
        buttons: ['Aceptar']
      });

      await alert.present();
    }
  }
}
