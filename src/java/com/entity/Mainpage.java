/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import java.util.Collection;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author agno3
 */
@Entity
@Table(name = "mainpage")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Mainpage.findAll", query = "SELECT m FROM Mainpage m")
    , @NamedQuery(name = "Mainpage.findByMainId", query = "SELECT m FROM Mainpage m WHERE m.mainId = :mainId")
    , @NamedQuery(name = "Mainpage.findByMainCollection", query = "SELECT m FROM Mainpage m WHERE m.mainCollection = :mainCollection")
    , @NamedQuery(name = "Mainpage.findByMainFollowexpert", query = "SELECT m FROM Mainpage m WHERE m.mainFollowexpert = :mainFollowexpert")
    , @NamedQuery(name = "Mainpage.findByMainClassRecord", query = "SELECT m FROM Mainpage m WHERE m.mainClassRecord = :mainClassRecord")
    , @NamedQuery(name = "Mainpage.findByMainBuyRecord", query = "SELECT m FROM Mainpage m WHERE m.mainBuyRecord = :mainBuyRecord")
    , @NamedQuery(name = "Mainpage.findByMainInventory", query = "SELECT m FROM Mainpage m WHERE m.mainInventory = :mainInventory")})
public class Mainpage implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 25)
    @Column(name = "main_id")
    private String mainId;
    @Size(max = 200)
    @Column(name = "main_collection")
    private String mainCollection;
    @Size(max = 200)
    @Column(name = "main_followexpert")
    private String mainFollowexpert;
    @Size(max = 200)
    @Column(name = "main_class_record")
    private String mainClassRecord;
    @Size(max = 200)
    @Column(name = "main_buy_record")
    private String mainBuyRecord;
    @Size(max = 200)
    @Column(name = "main_inventory")
    private String mainInventory;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "mainpageMainId")
    private Collection<Administrator> administratorCollection;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "mainpageMainId")
    private Collection<Expert> expertCollection;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "mainpageMainId")
    private Collection<User> userCollection;

    public Mainpage() {
    }

    public Mainpage(String mainId) {
        this.mainId = mainId;
    }

    public String getMainId() {
        return mainId;
    }

    public void setMainId(String mainId) {
        this.mainId = mainId;
    }

    public String getMainCollection() {
        return mainCollection;
    }

    public void setMainCollection(String mainCollection) {
        this.mainCollection = mainCollection;
    }

    public String getMainFollowexpert() {
        return mainFollowexpert;
    }

    public void setMainFollowexpert(String mainFollowexpert) {
        this.mainFollowexpert = mainFollowexpert;
    }

    public String getMainClassRecord() {
        return mainClassRecord;
    }

    public void setMainClassRecord(String mainClassRecord) {
        this.mainClassRecord = mainClassRecord;
    }

    public String getMainBuyRecord() {
        return mainBuyRecord;
    }

    public void setMainBuyRecord(String mainBuyRecord) {
        this.mainBuyRecord = mainBuyRecord;
    }

    public String getMainInventory() {
        return mainInventory;
    }

    public void setMainInventory(String mainInventory) {
        this.mainInventory = mainInventory;
    }

    @XmlTransient
    public Collection<Administrator> getAdministratorCollection() {
        return administratorCollection;
    }

    public void setAdministratorCollection(Collection<Administrator> administratorCollection) {
        this.administratorCollection = administratorCollection;
    }

    @XmlTransient
    public Collection<Expert> getExpertCollection() {
        return expertCollection;
    }

    public void setExpertCollection(Collection<Expert> expertCollection) {
        this.expertCollection = expertCollection;
    }

    @XmlTransient
    public Collection<User> getUserCollection() {
        return userCollection;
    }

    public void setUserCollection(Collection<User> userCollection) {
        this.userCollection = userCollection;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (mainId != null ? mainId.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Mainpage)) {
            return false;
        }
        Mainpage other = (Mainpage) object;
        if ((this.mainId == null && other.mainId != null) || (this.mainId != null && !this.mainId.equals(other.mainId))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.Mainpage[ mainId=" + mainId + " ]";
    }
    
}
