import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UserListComponent } from './user-list/user-list.component';
import { UserDetailComponent } from './user-detail/user-detail.component';
import { UserReservaComponent } from './user-reserva/user-reserva.component'; 

const routes: Routes = [
  {
    path: '',
    component: UserListComponent
  },
  {
    path: 'profile',
    component: UserDetailComponent
  },
  {
    path: 'reserva',
    component: UserReservaComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
