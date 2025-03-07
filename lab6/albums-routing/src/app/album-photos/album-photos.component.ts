import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GetDataService } from '../service/get-data.service';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html'
})
export class AlbumPhotosComponent implements OnInit {
  photos: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private dataService: GetDataService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.dataService.getPhotos(id).subscribe((data) => {
      this.photos = data;
    });
  }

  goBack(): void {
    this.router.navigate([`/albums/${this.route.snapshot.paramMap.get('id')}`]);
  }
}
