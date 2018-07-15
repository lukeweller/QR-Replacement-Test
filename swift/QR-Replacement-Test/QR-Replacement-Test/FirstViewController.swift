//
//  FirstViewController.swift
//  QR-Replacement-Test
//
//  Created by Luke Weller on 7/1/18.
//  Copyright © 2018 Luke Weller. All rights reserved.
//

import UIKit
import Toucan

class FirstViewController: UIViewController {

    @IBOutlet weak var testPhotoPicker: UISegmentedControl!
    @IBOutlet weak var testPhotoImage: UIImageView!
    @IBOutlet weak var testPhotoImageFull: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.testPhotoImage.image = UIImage(named: "insta0")
        self.testPhotoImage.layer.cornerRadius = self.testPhotoImage.frame.width / 2
        self.testPhotoImage.layer.masksToBounds = true
        
        self.testPhotoImageFull.image = Toucan(image: UIImage(named: "insta0")!).maskWithEllipse(borderWidth: 10, borderColor: UIColor.black).image
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func testPhotoPickerAction(_ sender: Any) {
        
        switch testPhotoPicker.selectedSegmentIndex  {
        case 0:
            self.testPhotoImage.image = UIImage(named: "insta0")
            self.testPhotoImageFull.image = UIImage(named: "insta0")
        case 1:
            self.testPhotoImage.image = UIImage(named: "insta1")
            self.testPhotoImageFull.image = UIImage(named: "insta1")
        case 2:
            self.testPhotoImage.image = UIImage(named: "insta2")
            self.testPhotoImageFull.image = UIImage(named: "insta2")
        default:
            self.testPhotoImage.image = UIImage(named: "insta0")
            self.testPhotoImageFull.image = UIImage(named: "insta0")
        }
        
    }
    
}

