import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GetDataService } from '../service/get-data.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html'
})
export class AlbumDetailComponent implements OnInit {
  album: any = {};
  newTitle: string = '';

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private dataService: GetDataService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.dataService.getAlbum(id).subscribe((data) => {
      this.album = data;
      this.newTitle = data.title;
    });
  }

  saveTitle(): void {
    this.dataService.updateAlbum(this.album.id, this.newTitle).subscribe(() => {
      alert('Title updated!');
    });
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }

  goToPhotos(): void {
    this.router.navigate([`/albums/${this.album.id}/photos`]);
  }
}
